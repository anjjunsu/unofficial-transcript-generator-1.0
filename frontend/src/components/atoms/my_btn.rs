use yew::prelude::*;

#[derive(Properties, PartialEq)]
pub struct Props {
    pub label: String,
}

#[function_component(MyBtn)]
pub fn my_btn(props: &Props) -> Html {
    html! {
        <button>{props.label.clone()}</button>
    }
}
