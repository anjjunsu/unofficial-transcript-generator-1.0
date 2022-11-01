use crate::components::atoms::{file_input::FileInput, my_btn::MyBtn};
use gloo::console::log;
use wasm_bindgen::{JsCast, JsValue};
use web_sys::File;
use yew::prelude::*;

#[function_component(FileForm)]
pub fn file_form() -> Html {
    let file_state: UseStateHandle<File> = use_state(|| {
        // set default value for file
        let file = File::new_with_str_sequence(&JsValue::from_str(""), "defaultFile").unwrap();
        file
    });

    let cloned_file_state = file_state.clone();

    let file_changed = Callback::from(move |file| {
        cloned_file_state.set(file);
    });

    html! {
        <form>
            <FileInput
                name="file_from"
                handle_onchange={file_changed} />
            <MyBtn label="Submit" />
        </form>
    }
}
