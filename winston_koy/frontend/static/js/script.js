window.onload = function() {

	var btn = $( '.btn' );

	var btnFront = $( '.btn-front' ),
		btnYes = $( '.btn-back .yes' ),
		btnNo = $( '.btn-back .no' );

		btn.each(function(event){
			$(this).click(function(){
				console.log('test')
			var mx = event.clientX - btn.offsetLeft,
				my = event.clientY - btn.offsetTop;

			var w = btn.offsetWidth,
				h = btn.offsetHeight;

			var directions = [
				{ id: 'top', x: w/2, y: 0 },
				{ id: 'right', x: w, y: h/2 },
				{ id: 'bottom', x: w/2, y: h },
				{ id: 'left', x: 0, y: h/2 }
			];

			directions.sort( function( a, b ) {
				return distance( mx, my, a.x, a.y ) - distance( mx, my, b.x, b.y );
			} );

				btn.attr( 'data-direction', directions.shift().id );
				btn.toggleClass( "is-open" );
			} );
		})
	

	btnYes.click(function( event ) {
		btn.classList.remove( 'is-open' );
	} );

	btnNo.click(function( event ) {
		btn.classList.remove( 'is-open' );
	} );

	function distance( x1, y1, x2, y2 ) {
		var dx = x1-x2;
		var dy = y1-y2;
		return Math.sqrt( dx*dx + dy*dy );
	}

};