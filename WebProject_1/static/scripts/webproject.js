$("#accordion").accordion();



var availableTags = [
    "ActionScript",
    "AppleScript",
    "Asp",
    "BASIC",
    "C",
    "C++",
    "Clojure",
    "COBOL",
    "ColdFusion",
    "Erlang",
    "Fortran",
    "Groovy",
    "Haskell",
    "Java",
    "JavaScript",
    "Lisp",
    "Perl",
    "PHP",
    "Python",
    "Ruby",
    "Scala",
    "Scheme"
];
$("#autocomplete").autocomplete({
    source: availableTags
});



$("#button").button();
$("#button-icon").button({
    icon: "ui-icon-gear",
    showLabel: false
});



$("#radioset").buttonset();



$("#controlgroup").controlgroup();



$("#tabs").tabs();



$("#dialog").dialog({
    autoOpen: false,
    width: 400,
    buttons: [
        {
            text: "Ok",
            click: function () {
                $(this).dialog("close");
            }
        },
        {
            text: "Cancel",
            click: function () {
                $(this).dialog("close");
            }
        }
    ]
});

// Link to open the dialog
$("#dialog-link").click(function (event) {
    $("#dialog").dialog("open");
    event.preventDefault();
});



$("#datepicker").datepicker({
    inline: true
});



$("#slider").slider({
    range: true,
    values: [17, 67]
});



$("#progressbar").progressbar({
    value: 20
});



$("#spinner").spinner();



$("#menu").menu();



$("#tooltip").tooltip();



$("#selectmenu").selectmenu();


// Hover states on the static widgets
$("#dialog-link, #icons li").hover(
    function () {
        $(this).addClass("ui-state-hover");
    },
    function () {
        $(this).removeClass("ui-state-hover");
    }
);


// Accepted additional formats [here, allow for example "4/7/18" for "July 4, 2018"]
$.datepicker.additionalFormats = ["ddmmy", "ddmmyy", "d/m/y", "d/m/yy", "d/mm/y", "dd/m/y", "dd/m/yy", "dd/mm/y"];
// Backup the original parsing function
$.datepicker.originalParseDate = $.datepicker.parseDate;
// New parsing function
$.datepicker.parseDate = function (format, value, settings) {
    // Function that returns a date based on an input format
    function testParse(inputFormat) {
        try {
            // Try to get the date based on the input format
            date = $.datepicker.originalParseDate(inputFormat, value, settings);
            // If the date is right, returns it immediately
            return date;
        }
        catch (Error) {
            // _RD Bad date (this line does nothing but catching the error)
        }
    }
    // Initialise the returned date
    var date;
    // Don't bother with empty values
    if (value !== "0" && value !== "") {
        // Test the main datepicker format (which is an argument of this function)
        testParse(format);
        // If the main datepicker format didn't work, try with the additional ones
        for (var n = 0; n < $.datepicker.additionalFormats.length; n++) {
            testParse($.datepicker.additionalFormats[n]);
        }
    }
    // If the input string couldn't be parsed, returns just the "undefined"-typed variable
    return date;
};