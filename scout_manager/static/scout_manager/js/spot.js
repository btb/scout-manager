var Spot = {
    submit_spot: function (e) {
        var form_data = Spot.get_edit_form_data();
        console.log(form_data);
        $.ajax({
            url: "/manager/api/spot/" + form_data.id,
            type: "PUT",
            data: JSON.stringify(form_data),
            contentType: "application/json",
            dataType: "json",
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
            success: function(results) {
                console.log('success');
            },
            error: function(xhr, status, error) {
            }
        });
    },

    get_edit_form_data: function() {
        var form = $("form").first();
        var serialized_form = form.serializeObject();
        serialized_form["hours"] = Spot._get_spot_hours();
        return serialized_form;

    },

    _get_spot_hours: function() {
        var days = $("fieldset.mgr-hours");
        var avalible_hours = {};
        $.each(days, function(idx, day_fieldset){
            var day_name = $(day_fieldset).attr("data-day");
            var hours_blocks = $(day_fieldset).find(".mgr-hours-block");
            avalible_hours[day_name] = [];
            $.each(hours_blocks, function(idx, block){
                var inputs = $(block).find("input");
                var start = $(inputs[0]).val();
                var end = $(inputs[1]).val();
                avalible_hours[day_name].push([start, end]);
            });

        });
        return avalible_hours;

    },

    init_events: function () {
        $("input[value='Publish']").click(Spot.submit_spot);
    }
}