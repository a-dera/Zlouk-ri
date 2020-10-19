/*  vue file for texts*/

//titles
var title = new Vue({
		  delimiters: ['[[', ']]'],
		  el: 'title',
		  data: {
			title: "Zlouk'ri"
  
		  }
		})
var title = new Vue({
		  delimiters: ['[[', ']]'],
		  el: '#colorlib-logo',
		  data: {
			name: "Zlouk'ri"
  
		  }
		})

//First plan
var firstPlan = new Vue({
	      delimiters: ['[[', ']]'],
		  el: '#home',
		  data: {
			a: "You have a project, but not yet a name for this ambitious project?",
            b: "Don't worry, generate a brandable business name powerred by artificial intellenge ",
			d: "test"
  
		  }
		})

//features
var features = new Vue({
	 	  delimiters: ['[[', ']]'],
		  el: '#features',
		  data: {
            CreateUniqueNames: 'Create unique name for your project.',
            PrioritizinSshortNames :'Short names are memorable and affordable.',
            FilteringOptions:'use the filter tools to adjust and refine the results',
            LotsOfFeatures:'Many others features are in progress. Keep in touch',
            ExportForUse:'Export the best suggestions for later use without moderation.',
            HelpSupport:'Ask for help at anytime you want and get advice.'
          }
		})

//Limitation
		var app = new Vue({
		  delimiters: ['[[', ']]'],
		  el: '#zloukri',
		  data: {
            limit: 'Separate each keyword with a simple comma'
		  }
		})

//key validation 
var validation = new Vue({
		  delimiters: ['[[', ']]'],
		  el: '#KeyValidation',
		  data: {
			key: "key1"
		  }
		})
	
//email
var mail = new Vue({
	 	  delimiters: ['[[', ']]'],
		  el: '#mail',
		  data: {
			mail: "dera.amedee@gmail.com"
		  }
		})