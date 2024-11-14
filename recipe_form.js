var ingredient_dropdown_list = []
var id_inc = 0
add_initial_dropdown = async () => {
	const id_number = id_inc
	id_inc += 1;
	const id = `ingred${id_number}`
	const unit_id = `unit${id_number}`
	const quantity_id = `quantity${id_number}`

	const response = await fetch('/all_ingredients');
	const option_list = await response.json()
	const new_select = new_dropdown(id, option_list)

	const label = document.getElementById("RecipeIngredientLabel")

	const unit = document.createElement('input')
	unit.id = unit_id

	const quantity = document.createElement('input')
	quantity.id = quantity_id

	const para = document.createElement("p")
	para.appendChild(new_select)
	para.appendChild(unit)
	para.appendChild(quantity)
	label.appendChild(para)
	ingredient_dropdown_list.push(new_select)
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

	const unit = document.createElement('input')
	unit.id = unit_id

	const quantity = document.createElement('input')
	quantity.id = quantity_id

	const para = document.createElement("p")
	para.appendChild(new_select)
	para.appendChild(unit)
	para.appendChild(quantity)
	ingredient_dropdown_list.slice(-1)[0].parentNode.parentNode.insertBefore(para, ingredient_dropdown_list.slice(-1)[0].parentNode.nextSibling)

	ingredient_dropdown_list.push(new_select)

	const remove = document.createElement("button")
	remove.type = "button"
	remove.onclick = () => {
		para.remove();
		ingredient_dropdown_list = ingredient_dropdown_list.filter(x => x.id !== id)
		if (ingredient_dropdown_list.length > 0) {
			ingredient_dropdown_list.slice(-1)[0].onchange = () => { add_dropdown(); }
		}
	}
	remove.innerText = '❌'
	para.appendChild(remove)

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



