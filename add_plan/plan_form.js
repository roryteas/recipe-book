//js for the add plan page

var plan_field_counter = 0


const add_plan_fieldset = async () => {
	const option_state = null
	plan_field_counter++
	const fieldset = document.createElement('fieldset')
	fieldset.id = 'plan' + plan_field_counter

	const response = await fetch('/all_recipes')

	const recipe_options = await response.json()

	const recipe_dropdown = document.createElement('select')

	var option_node = document.createElement("option")
	recipe_dropdown.appendChild(option_node)
	recipe_options.forEach((option) => {
		var option_node = document.createElement("option")
		option_node.value = option.id
		option_node.text = option.id + ". " + option.title
		console.log(option.title)
		console.log(option.id)
		recipe_dropdown.appendChild(option_node)
	})
	fieldset.appendChild(recipe_dropdown)
	const recipe_details = document.createElement('div')
	recipe_details.style.display = 'none'

	const recipe_details_change = (option) => {
		const recipe = recipe_options.filter((x) => x.id == option)[0]
		recipe_details.innerHTML = ''
		const table = document.createElement('table')
		const head = document.createElement('thead')
		head.innerHTML = '<tr><td>Ingredient</td><td>Unit</td><td>Quantity</td></tr>'
		table.appendChild(head)
		if (recipe != undefined) {
			recipe.ingredients.forEach((x) => {
				console.log(x)
				row = document.createElement('tr')
				row.innerHTML = '<td>' + x.name + '</td>' + '<td>' + x.unit + '</td>' + '<td>' + x.quantity + '</td>'
				table.appendChild(row)
			})


			recipe_details.appendChild(table)
			const recipe_text = document.createElement('p')
			recipe_text.innerText = recipe.recipe_text
			recipe_details.appendChild(recipe_text)
		}
	}
	recipe_dropdown.onchange = (e) => recipe_details_change(e.target.value)

	const accordion = document.createElement("button")
	accordion.class = 'accordion'
	accordion.type = 'button'
	accordion.innerText = '▼'
	const toggle_expanded = () => {
		recipe_details.style.display === 'none' ? recipe_details.style.display = 'block' : recipe_details.style.display = 'none'
	}

	accordion.onclick = toggle_expanded
	fieldset.appendChild(accordion)
	fieldset.appendChild(recipe_details)


	const plan_container = document.getElementById('plan_container')
	plan_container.appendChild(fieldset)

}

const submit_plan = async () => {
	console.log("e")
}
