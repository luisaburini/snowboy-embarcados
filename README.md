# README #

This Proof of Concept tests the [Snowboy API](https://github.com/Kitt-AI/snowboy) with [Apalis iMX6](https://developer.toradex.com/products/apalis-imx6) detecting 2 different hotwords. When it detects "Apalis acende led", one more (limited to 5) led will be lit, and when it detects "Apalis apaga led", the last lit led will be turned off.
To solve the dependencies, please check SNOWBOY_SETUP file in repository.

### How to use the demo ###

* Module: Apalis iMX6
* Carrier Board: [Apalis Evaluation Board](https://developer.toradex.com/products/apalis-evaluation-board) or [Ixora Carrier Board](https://developer.toradex.com/products/ixora-carrier-board)
* Aditional materials: microphone (or UVC Web Cam)

### How do I get set up? ###

* Please read SNOWBOY_SETUP to remove dependencies and run ./init.sh
