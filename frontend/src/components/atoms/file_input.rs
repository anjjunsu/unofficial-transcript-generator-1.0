use yew::prelude::*;

#[derive(Properties, PartialEq)]
pub struct Props {
    pub name: String,
}

#[function_component(FileInput)]
pub fn file_input(props: &Props) -> Html {
    html! {
        <input type="file" name={props.name.clone()} />
    }
}
