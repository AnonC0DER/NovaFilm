window.addEventListener('load', function() {

	const sliderRadios = document.getElementsByClassName("slider-radio");
	const animationDuration = 0.2;
	let timeout = null;

	for (let i = 0; i < sliderRadios.length; i++) {
		let sliderRadio = sliderRadios[i];

		const slidingPiece = document.createElement('div');
		slidingPiece.className = "sliding-piece";
		sliderRadio.appendChild(slidingPiece);
		slidingPiece.style.position = "absolute";
		slidingPiece.style.transition = "width " + animationDuration + "s, height " + animationDuration + "s, top " + animationDuration + "s, left " + animationDuration + "s";

		sliderRadio.addEventListener('click', handleLabelClick);

		// Simply setting up the `sliderPiece` by clicking any pre-checked value;
		const radios = sliderRadio.querySelectorAll("input[type='radio']");
		for(let i = 0; i < radios.length; i++) {if(radios[i].checked) radios[i].click() }
	}

	function handleLabelClick(e) {
		let label;
		let radio;
		let slidingPiece;

		if (e.target.nodeName === "INPUT") {

			radio = e.target;
			label = radio.nextSibling;
			slidingPiece = radio.parentNode.querySelector(".sliding-piece");

			if(radio.checked) {
				const labelCoords = getElementCoords(label);

				// Read function description below.
				runUglyAnimationSetups(slidingPiece, );

				animateSlidingPiece(labelCoords);

				if (timeout) {
					clearTimeout(timeout);
				}
				timeout = setTimeout(function() {
					clearUglyAnimationSetups();

					timeout = null;
				}, (animationDuration+0.3) * 1000);

			}

		}

		function updateSlidingPieceCoords(label) {
			animateSlidingPiece(getElementCoords(label));
		}

		function animateSlidingPiece(coords) {
			slidingPiece.style.left = coords.x + "px";
			slidingPiece.style.top = coords.y + "px";
			slidingPiece.style.width = coords.width + "px";
			slidingPiece.style.height = coords.height + "px";
		}

		/**
		 * This function tries to hide the checked label until the animation
		 * is over, because, in truth, the label is checked instantly. So
		 * it gets all the styles from the css. But things like border or background-color
		 * we don't want to show up instantly. So in this function we hide those styles.
		 */
		function runUglyAnimationSetups() {
			slidingPiece.style['transition-duration'] = animationDuration;
			slidingPiece.style.opacity = 1;
			label.style.backgroundColor = "transparent";
			label.style.boxShadow = "none";
			label.style.borderColor = "transparent";
		}

		function clearUglyAnimationSetups() {
			label.style.backgroundColor = "";
			slidingPiece.style.opacity = '0';
			label.style.boxShadow = "";
			label.style.borderColor = "";
		}

	}

	function getElementCoords(el) {
		const elementPosition =  {x: el.offsetLeft, y: el.offsetTop};
		const elementSize = el.getBoundingClientRect();

		return {
			x: elementPosition.x,
			y: elementPosition.y,
			width: elementSize.width,
			height: elementSize.height
		}
	}
});