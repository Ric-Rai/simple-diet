$(init);

function init() {

    $(".data-table").dataTable();

    /* Diet */
    const $main = $("#main"),
          $diet = $("#diet");

    // Delete meal on delete button click
    $diet.on("click", ".delete-meal", function (ev) {
        const $row = $(ev.target).closest(".data-table"), id = $row.attr("row-id");
        $.post('/meals/delete', 'id=' + id).done(() => {
            $.get(document.location, (html) => {
                let doc  = $('<div></div>').append($.parseHTML(html));
                $main.replaceWith(doc.find("#main"));
                init();
            })
        });
    });

    // Add meal to diet on add button click
    $("#add-meal").click((ev) => $.get($(ev.target).attr("add-url"), (html) =>
        $(html).appendTo($diet).dataTable()));

}


$.fn.dataTable = function() {
    this.each(function () {

        const $main = $("#main"),
              $diet = $("#diet"),
              $foods = $(".foods"),
              $table = $(this).find("table:first"),
              URL = "/" + $table.attr('url'),
              $addRowButton = $(this).find(".add-row:first"),
              editOff = ($inputRow, $row) => {
                  //if ($inputRow.attr("id") !== "input-row") return;
                  if ($foods.length) {
                      $inputRow.replaceWith($row);
                      $("#error-row").remove();
                      $addRowButton.removeAttr("disabled")
                  } else {
                      $.get(document.location, (html) => {
                          let doc = $('<div></div>').append($.parseHTML(html));
                          $main.replaceWith(doc.find("#main"));
                          init();
                      })
                  }
              },
              editOn = ($inputRow, $row) => {
                  if ($("#input-row").length) return;
                  if (!$inputRow.attr("row-id")) {
                      if ($diet.length) $table.append($inputRow);
                      else $table.prepend($inputRow);
                  }
                  else $row.replaceWith($inputRow);
                  $addRowButton.attr("disabled", "disabled");
              },
              error = ($inputRow, $errorRow) => {
                if(!$("#error-row").replaceWith($errorRow).length) $inputRow.before($errorRow)
              };

        // Prepend table with input row on add new button click
        $addRowButton.click((ev) => {
            const addURL = $(ev.target).attr("add-url");
            if (addURL) $.get(addURL, (html) => {
                console.log(html);
                editOn($(html))
            });
            else $.get(URL + "/new", (html) => editOn($(html)));
        });

        // Edit row on edit button click
        $(this).on("click", ".edit", (ev) => {
            const $row = $(ev.target).closest("tr");
            console.log(URL + "/edit" + $row.find("input").serialize());
            $.get(URL + "/edit", $row.find("input").serialize(), (html) =>  editOn($(html), $row ))
        });

        // Submit on add button click
        $(this).on("click", ".add", function () {
            const $inputRow = $("#input-row"), id = $inputRow.attr("row-id");
            $inputRow.find("input[current-time]")
                .val(new Date(Date.now()).toISOString().substr(0, 16).replace(/[:T]/g, "-"));
            console.log($inputRow.find("input[current-time]").val());
            console.log($inputRow.find("input").serialize());
            $.post(id ? URL + "/edit": URL + "/new", $inputRow.find("input").serialize())
                .done((html) => editOff($inputRow, $(html)))
                .fail((res) => error($inputRow, $(res.responseText)));
        });

        // Delete row on delete button click
        $(this).on("click", ".delete", function () {
            const $row = $(this).closest("tr"), id = $row.attr("row-id");
            if (!id) editOff($row.remove());
            else $.post(URL + '/delete', $row.find("input#id").serialize())
                .done(() => {
                    $row.remove();
                    $("#error-row").remove();
                    $addRowButton.removeAttr("disabled")
                });
        });


    });
};