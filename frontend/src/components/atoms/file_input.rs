use wasm_bindgen::JsCast;
use web_sys::{File, HtmlInputElement};
use yew::prelude::*;

#[derive(Properties, PartialEq)]
pub struct Props {
    pub name: String,
    pub handle_onchange: Callback<File>,
}

#[function_component(FileInput)]
pub fn file_input(props: &Props) -> Html {
    let handle_onchange = props.handle_onchange.clone();

    let onchange = Callback::from(move |event: Event| {
        let value = event
            .target()
            .unwrap()
            .unchecked_into::<HtmlInputElement>()
            .files()
            .unwrap()
            .get(0)
            .unwrap();

        handle_onchange.emit(value);
    });
    html! {
        <input
            onchange={onchange}
            type="file"
            name={props.name.clone()} />
    }
}
