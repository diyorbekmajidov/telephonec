(function($) {
    $(document).ready(function() {
        console.log("JS ishladi!");

        function filterManagement() {
            var statusField = $("#id_status");
            var managementField = $("#id_management");

            if (!statusField.length || !managementField.length) return;

            var statusValue = statusField.val();
            console.log("Status tanlandi:", statusValue);

            // Barcha variantlarni yashirish
            managementField.find("option").hide();

            if (statusValue === "2") {
                // Agar status 2 bo‘lsa, hech narsa ko‘rsatmaymiz
                managementField.val("");
            } else {
                managementField.find("option").each(function() {
                    var optionType = $(this).attr("data-type"); // `data-type` ni olamiz

                    if (
                        (statusValue === "1" && optionType === "1") || 
                        (statusValue === "3" && optionType === "3")
                    ) {
                        $(this).show();
                    }
                });

                // Yashirin bo‘lmagan birinchi elementni tanlash
                var firstVisible = managementField.find("option:visible:first").val();
                managementField.val(firstVisible);
            }
        }

        $("#id_status").change(filterManagement);
        filterManagement();
    });
})(django.jQuery);
