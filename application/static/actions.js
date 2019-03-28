$(function () {

    const $addRowButton = $("#add-row"),
          editOff = ($inputRow, $row) => {
            if ($inputRow.attr("id") !== "input-row") return;
            $inputRow.replaceWith($row);
            $("#error-row").remove();
			$addRowButton.removeAttr("disabled") },
          editOn = ($inputRow, $row) => {
            if ($("#input-row").length) return;
            if (!$inputRow.attr("row-id")) $inputRow.prependTo("table");
            else $row.replaceWith($inputRow);
            $addRowButton.attr("disabled", "disabled");
          },
          error = ($inputRow, $errorRow) => {
            if(!$("#error-row").replaceWith($errorRow).length) $inputRow.before($errorRow)
          };

    // Prepend table with input row on add new button click
    $addRowButton.click(() => $.get('/foods/input-row', (html) => editOn($(html).find("tr"))));

    // Edit row on edit button click
    $(document).on("click", ".edit", (ev) => {
        const $row = $(ev.target).parents("tr");
        $.get('/foods/input-row/' + $row.attr("row-id"), (html) => editOn($(html).find("tr"), $row))
    });

    // Submit on add button click
    $(document).on("click", ".add", function () {
        const $inputRow = $("#input-row"), id = $inputRow.attr("row-id");
        $.post(id ? "/foods/input-row/" + id : "/foods/input-row", $inputRow.find("input").serialize())
            .done((html) => editOff($inputRow, $(html).find("tr")))
            .fail((res) => error($inputRow, $(res.responseText).find("#error-row")));
    });

    // Delete row on delete button click
    $(document).on("click", ".delete", function () {
        const $row = $(this).parents("tr"), id = $row.attr("row-id");
        if(!id) editOff($row.remove());
        else $.post('/foods/delete/' + id).done(() => editOff($row.remove()));
    });

});