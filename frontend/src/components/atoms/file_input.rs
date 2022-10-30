use wasm_bindgen::JsCast;
use web_sys::{EventTarget, HtmlInputElement, Url};
use yew::prelude::*;
use yew::{events::Event, html};

use gloo::console::log;

#[derive(Properties, PartialEq)]
pub struct Props {
    pub name: String,
}

#[function_component(FileInput)]
pub fn file_input(props: &Props) -> Html {
    let on_change = Callback::from(|event: Event| {
        log!("Starting on change");

        event.prevent_default();

        let target: EventTarget = event
            .target()
            .expect("Event should have a target when dispatched");

        let files = target
            .unchecked_into::<HtmlInputElement>()
            .files()
            .expect("Failed to read file");

        // let file = files.item(0).expect("Failed to get file from file list");

        // let content = file.stream();
        // log!(content);
    });

    html! {
        <input
            onchange={on_change}
            type="file"
            name={props.name.clone()} />
    }
}
