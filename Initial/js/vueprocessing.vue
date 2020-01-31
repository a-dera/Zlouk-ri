/*  fichier de traitement des rendus Vue*/

//traitement du titre
var title = new Vue({
		  el: 'title',
		  data: {
			title: "Zlouk'ri"
  
		  }
		})

//traitement du titre
var title = new Vue({
		  el: '#colorlib-logo',
		  data: {
			name: "Zlouk'ri"
  
		  }
		})

//premier plan
var firstPlan = new Vue({
		  el: '#home',
		  data: {
			a: "You have a project, but not yet a name for this ambitious project?",
            b: "Don't worry, generate a brandable business name powerred by artificial intellenge ",
			d: "test"
  
		  }
		})

//features
var features = new Vue({
		  el: '#features',
		  data: {
            CreateUniqueNames: 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
            PrioritizinSshortNames :'In 2019 many startups are choosing a short, branded name - a name that’s unique, memorable and affordable.',
            FilteringOptions:'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
            LotsOfFeatures:'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
            ExportForUse:'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.',
            HelpSupport:'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.'
          }
		})

//Limitation
		var app = new Vue({
		  el: '#colorlib-subscribe',
		  data: {
			message: 'Hello Vue !',
            limit: 'Limitation -- 4'
		  }
		})

//validation des keys
var validation = new Vue({
		  el: '#KeyValidation',
		  data: {
			key: "key1"
		  }
		})
	
//email
var mail = new Vue({
		  el: '#mail',
		  data: {
			mail: "dera.amedee@gmail.com"
		  }
		})