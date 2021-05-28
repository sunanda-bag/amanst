jQuery(document).ready(function () {
	$(".ajaxLoader").hide();
	// Product Filter Start
	$(".filter-checkbox").on('click', function () {
		var _filterObj = {};
		$(".filter-checkbox").each(function (index, ele) {
			var _filterVal = $(this).val();
			var _filterKey = $(this).data('filter');
			
			_filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
				return el.value;
			});
			
		});
		console.log(_filterObj)

		// Run Ajax
		$.ajax({
			url: '/jobs-filter',
			data: _filterObj,
			dataType: 'json',
			beforeSend: function () {
				 $(".ajaxLoader").show();
			},
			success: function (res) {
				console.log('hii');
				console.log(res);
				$("#customers").html(res.data);
				 $(".ajaxLoader").hide();
			}
		});
	});
	// End
});