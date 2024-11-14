const post_ingredient = async(name) => {
	let data = new FormData()
	data.append("name",name.value)
	const response = await fetch("/add_ingredient", {method: "POST", body: data})
}

const ingredient_form_submit = () => {post_ingredient(document.forms["ingredient_form"]["name"])}
