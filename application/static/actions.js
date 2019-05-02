$(init);

function init() {

    const $diet = $("#diet");
    if ($diet.length) {
        $.getScript("/static/jquery.easy-autocomplete.min.js");
        $.getJSON("/foods/list").done((data) => window.foodList = data);
    }

    $(".data-table").dataTable();

    // Delete meal on delete button click
    $diet.on("click", ".delete-meal", function (ev) {
        const $row = $(ev.target).closest(".data-table"), id = $row.attr("row-id");
        $.post('/meals/delete', 'id=' + id).done(() => {
            $row.remove();
            calculateMacros($row, $diet)
        });
    });

    // Add meal to diet on add button click
    $("#add-meal").click((ev) => $.get($(ev.target).attr("add-url"), (html) =>
        $(html).appendTo($diet).dataTable()));

}

function calculateMacros($row, $diet) {
    const $meal = $row.closest(".meal");
    $.get(document.location, (html) => {
        let $doc = $('<div></div>').append($.parseHTML(html));
        const $mealRow = $meal.closest("tr");
        const $newMealRow = $doc.find(".data-table[row-id=" + $mealRow.attr("row-id") + "]");
        $meal.find(".meal-energy").html($newMealRow.find(".meal-energy").html());
        $meal.find(".meal-protein").html($newMealRow.find(".meal-protein").html());
        $meal.find(".meal-carb").html($newMealRow.find(".meal-carb").html());
        $meal.find(".meal-fat").html($newMealRow.find(".meal-fat").html());
        $diet.find("#diet-energy").html($doc.find("#diet-energy").html());
        $diet.find("#diet-protein").html($doc.find("#diet-protein").html());
        $diet.find("#diet-carb").html($doc.find("#diet-carb").html());
        $diet.find("#diet-fat").html($doc.find("#diet-fat").html());
    });
}


$.fn.dataTable = function () {
    this.each(function () {

        const $diet = $("#diet"),
            $foods = $(".foods"),
            $diets = $(".diets"),
            $table = $(this).find("table:first"),
            URL = "/" + $table.attr('url'),
            $addRowButton = $(this).find(".add-row:first"),
            editOff = ($inputRow, $row) => {
                if ($foods.length || $diets.length) {
                    const $inputs = $inputRow.find("input");
                    let hasChanged = false;
                    $inputs.each((i, e) => { if ($(e).attr("value") !== $(e).val()) hasChanged = true });
                    if (hasChanged) $row.addClass("new-row");
                }
                if ($row.eq(0).is("tr")) $inputRow.replaceWith($row);
                if ($diet.length) calculateMacros($row, $diet);
                $("#error-row").remove();
                $addRowButton.removeAttr("disabled");
            },
            editOn = ($inputRow, $row) => {
                if ($("#input-row").length) return;
                if (!$inputRow.attr("row-id")) {
                    if ($diet.length) $table.append($inputRow);
                    else $table.prepend($inputRow);
                } else if ($row.eq(0).is("tr")) $row.replaceWith($inputRow);
                if ($diet.length)
                    $inputRow.find("#food_name").easyAutocomplete({
                        data: window.foodList,
                        list: {
                            match: {
                                enabled: true
                            }
                        }
                    });
                $addRowButton.attr("disabled", "disabled");
            },
            error = ($inputRow, $errorRow) => {
                if (!$errorRow.eq(0).is("tr")) return;
                if (!$("#error-row").replaceWith($errorRow).length) $inputRow.before($errorRow)
            };

        // Prepend table with input row on add new button click
        $addRowButton.click((ev) => {
            const addURL = $(ev.target).attr("add-url");
            if (addURL) $.get(addURL, (html) => editOn($(html)));
            else $.get(URL + "/new", (html) => editOn($(html)));
        });

        // Edit row on edit button click
        $(this).on("click", ".edit", (ev) => {
            const $row = $(ev.target).closest("tr");
            $.get(URL + "/edit", $row.find("input").serialize(), (html) => {
                const $inputRow = $(html);
                editOn($inputRow, $row)
            })
        });

        // Submit on add button click
        $(this).on("click", ".add", function () {
            const $inputRow = $("#input-row"), id = $inputRow.attr("row-id"),
                $dateTimeInput = $inputRow.find("input[current-time]");
            if ($dateTimeInput.length !== 0 && $dateTimeInput.val().length === 0) {
                const dt = new Date(Date.now()),
                    date = pad(dt.getDate(), 2) + "." + pad(dt.getMonth() + 1, 2) + "." + dt.getFullYear(),
                    time = pad(dt.getHours(), 2) + ":" + pad(dt.getMinutes(), 2);
                $dateTimeInput.val(date + " " + time);
            }
            $.post(id ? URL + "/edit" : URL + "/new", $inputRow.find("input").serialize())
                .done((html) => editOff($inputRow, $(html)))
                .fail((res) => error($inputRow, $(res.responseText)));
        });

        function pad(n, width) {
            n = n + '';
            return n.length >= width ? n : new Array(width - n.length + 1).join("0") + n;
        }

        // Delete row on delete button click
        $(this).on("click", ".delete", function () {
            const $row = $(this).closest("tr"), id = $row.attr("row-id");
            if (!id) {
                $row.remove();
                $("#error-row").remove();
                $addRowButton.removeAttr("disabled");
            } else {
                $.post(URL + '/delete', $row.find("input#id").serialize())
                    .done(() => {
                        if ($diet.length) calculateMacros($row, $diet);
                        $row.remove();
                    });
            }
        });

    });
};