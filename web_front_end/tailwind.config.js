module.exports = {
	content: [
		'./components/*.js',
		'./pages/*.js',
		'./styles/*.css'
	],
	theme: {
		extend: {
			fontFamily: {
				lora: ['Lora', 'serif'],
				roboto: ['Roboto', 'sans-serif']
			},
			colors: {
				background: '#202020',
				title: '#AC3931',
				text: '#364156'
			},

		},
	},
	plugins: [],
}
