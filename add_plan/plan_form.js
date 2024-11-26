//js for the add plan page

var plan_field_counter = 0


const add_plan_fieldset = async () => {
	plan_field_counter++
	const fieldset = document.createElement('fieldset')
	fieldset.id = 'plan' + plan_field_counter

	const response = await fetch('/all_recipes')

	const recipe_options = await response.json()

	const recipe_dropdown = document.createElement('select')

	recipe_options.forEach((option) => {
		var option_node = document.createElement("option")
		option.value = option.id
		option.text = option.title
		recipe_dropdown.appendChild(option_node)
	})

	fieldset.appendChild(recipe_dropdown)

	const plan_container = document.getElementById('plan_container')
	plan_container.appendChild(fieldset)
}



