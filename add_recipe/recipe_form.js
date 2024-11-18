var ingredient_dropdown_list = []
var id_inc = 0

submit_recipe = async () => {
	const recipe_form_elements = document.getElementById(`recipe_form`).elements
	const recipe = { title: recipe_form_elements[0].value, ingredients: [], recipe_text: "" }
	var i = 1;
	while (i < recipe_form_elements.length - 2) {
		ingredient = { id: "", unit: "", quantity: 0 }
		ingredient.id = recipe_form_elements[i].value
		i++;
		ingredient.unit = recipe_form_elements[i].value
		i++;
		ingredient.quantity = recipe_form_elements[i].value
		i++;
		i++;
		if (ingredient.id !== "") { recipe.ingredients.push(ingredient) }

	}
	recipe.recipe_text = recipe_form_elements[i].value
	console.log(recipe)
	data = new FormData()
	data.append('recipe', JSON.stringify(recipe))
	await fetch("/add_recipe", { method: "POST", body: data })
}

add_initial_dropdown = async () => {
	const id_number = id_inc
	id_inc += 1;
	const id = `ingred${id_number}`
	const unit_id = `unit${id_number}`
	const quantity_id = `quantity${id_number}`

	const response = await fetch('/all_ingredients');
	const option_list = await response.json()
	const new_select = new_dropdown(id, option_list)
	const new_select_cell = document.createElement('td')
	new_select_cell.appendChild(new_select)

	const label = document.getElementById("RecipeIngredientLabel")

	const unit = document.createElement('input')
	unit.id = unit_id
	const unit_cell = document.createElement('td')
	unit_cell.appendChild(unit)
	const quantity = document.createElement('input')
	quantity.id = quantity_id
	const quantity_cell = document.createElement('td')
	quantity_cell.appendChild(quantity)

	const trow = document.createElement("tr")
	trow.appendChild(new_select_cell)
	trow.appendChild(unit_cell)
	trow.appendChild(quantity_cell)
	label.appendChild(trow)
	ingredient_dropdown_list.push(new_select)
	const remove = document.createElement("button")
	remove.type = "button"
	remove.onclick = () => {
		if (ingredient_dropdown_list.length > 1) {
			trow.remove();
			ingredient_dropdown_list = ingredient_dropdown_list.filter(x => x.id !== id)
			if (ingredient_dropdown_list.length > 0) {
				ingredient_dropdown_list.slice(-1)[0].onchange = () => { add_dropdown(); }
			}
		}
	}
	remove.innerText = '❌'

	const remove_cell = document.createElement('td')
	remove_cell.appendChild(remove);
	trow.appendChild(remove_cell)
}

add_dropdown = async () => {
	const id_number = id_inc
	id_inc += 1;
	const id = `ingred${id_number}`
	const unit_id = `unit${id_number}`
	const quantity_id = `quantity${id_number}`

	const response = await fetch('/all_ingredients');
	const option_list = await response.json()
	const new_select = new_dropdown(id, option_list)
	const new_select_cell = document.createElement('td')
	new_select_cell.appendChild(new_select)

	const unit = document.createElement('input')
	unit.id = unit_id
	const unit_cell = document.createElement('td')
	unit_cell.appendChild(unit)
	const quantity = document.createElement('input')
	quantity.id = quantity_id
	const quantity_cell = document.createElement('td')
	quantity_cell.appendChild(quantity)

	const trow = document.createElement("tr")
	trow.appendChild(new_select_cell)
	trow.appendChild(unit_cell)
	trow.appendChild(quantity_cell)
	ingredient_dropdown_list.slice(-1)[0].parentNode.parentNode.parentNode.insertBefore(trow, ingredient_dropdown_list.slice(-1)[0].parentNode.parentNode.nextSibling)

	ingredient_dropdown_list.push(new_select)

	const remove = document.createElement("button")
	remove.type = "button"
	remove.onclick = () => {
		if (ingredient_dropdown_list.length > 1) {
			trow.remove();
			ingredient_dropdown_list = ingredient_dropdown_list.filter(x => x.id !== id)
			if (ingredient_dropdown_list.length > 0) {
				ingredient_dropdown_list.slice(-1)[0].onchange = () => { add_dropdown(); }
			}
		}
	}
	remove.innerText = '❌'

	const remove_cell = document.createElement('td')
	remove_cell.appendChild(remove);
	trow.appendChild(remove_cell)

}

new_dropdown = (id, option_list) => {
	select = document.createElement('select')
	select.id = id
	select.onchange = () => { add_dropdown() };
	if (ingredient_dropdown_list.length > 0) {
		ingredient_dropdown_list.slice(-1)[0].onchange = null
	}
	var option = document.createElement("option")
	select.appendChild(option)
	for (var i = 0; i < option_list.length; i++) {
		var option = document.createElement("option")
		option.value = option_list[i].id
		option.text = option_list[i].name
		select.appendChild(option)
	}
	return select
}



