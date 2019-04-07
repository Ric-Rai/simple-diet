$(function () {
    $(".data-table").dataTable();

    /* Diet table */
    const $diet = $("#diet");

    // Delete meal on delete button click
    $diet.on("click", ".delete-meal", function (ev) {
        const $row = $(ev.target).closest(".data-table"), id = $row.attr("row-id");
        $.post('/meals/delete/' + id).done(() => $row.remove());
    });

    // Add meal to diet on add button click
    $("#add-meal").click(() =>
        $.get(window.location.href + '/meals/input-row', (html) =>
            $(html).appendTo($diet).dataTable()));

});

$.fn.dataTable = function() {
    this.each(function () {

        console.log("dataTable: "); console.log(this);
        const $table = $(this).find("table:first"),
              URL = $table.attr('url'),
              inputURL = "/" + URL + "/input-row",
              $addRowButton = $(this).find(".add-row:first"),
              editOff = ($inputRow, $row) => {
                if ($inputRow.attr("id") !== "input-row") return;
                $inputRow.replaceWith($row);
                $("#error-row").remove();
                $addRowButton.removeAttr("disabled") },
              editOn = ($inputRow, $row) => {
                if ($("#input-row").length) return;
                if (!$inputRow.attr("row-id")) $table.prepend($inputRow);
                else $row.replaceWith($inputRow);
                $addRowButton.attr("disabled", "disabled");
              },
              error = ($inputRow, $errorRow) => {
                if(!$("#error-row").replaceWith($errorRow).length) $inputRow.before($errorRow)
              };

        // Prepend table with input row on add new button click
        $addRowButton.click(() => $.get(inputURL, (html) => editOn($(html))));

        // Edit row on edit button click
        $(this).on("click", ".edit", (ev) => {
            const $row = $(ev.target).closest("tr");
            $.get(inputURL + '/' + $row.attr("row-id"), (html) => editOn($(html), $row))
        });

        // Submit on add button click
        $(this).on("click", ".add", function () {
            const $inputRow = $("#input-row"), id = $inputRow.attr("row-id");
            $inputRow.find("input[current-time]")
                .val(new Date(Date.now()).toISOString().substr(0, 16).replace(/[:T]/g, "-"));
            console.log($inputRow.find("input[current-time]").val());
            console.log($inputRow.find("input").serialize());
            $.post(id ? inputURL + '/' + id : inputURL, $inputRow.find("input").serialize())
                .done((html) => editOff($inputRow, $(html)))
                .fail((res) => error($inputRow, $(res.responseText)));
        });

        // Delete row on delete button click
        $(this).on("click", ".delete", function () {
            const $row = $(this).closest("tr"), id = $row.attr("row-id");
            if (!id) editOff($row.remove());
            else $.post('/' + URL + '/delete/' + id).done(() => editOff($row.remove()));
        });

    });


};