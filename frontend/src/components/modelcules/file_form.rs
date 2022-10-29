use crate::components::atoms::{file_input::FileInput, my_btn::MyBtn};
use wasm_bindgen::JsCast;
use web_sys::HtmlInputElement;
use yew::prelude::*;

#[function_component(FileForm)]
pub fn file_form() -> Html {
    let on_submit = Callback::from(|event: FocusEvent| {
        event.prevent_default();
        let value = event
            .target()
            .unwrap()
            .unchecked_into::<HtmlInputElement>()
            .value();
    });

    html! {
        <form onsubmit={on_submit}>
            <FileInput name="transcript_from" />
            <MyBtn label="Submit" />
        </form>
    }
}
