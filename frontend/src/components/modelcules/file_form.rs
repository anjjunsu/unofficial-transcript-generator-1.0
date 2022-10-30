use crate::components::atoms::{file_input::FileInput, my_btn::MyBtn};
use yew::prelude::*;

#[function_component(FileForm)]
pub fn file_form() -> Html {
    html! {
        <form>
            <FileInput name="transcript_from" />
            <MyBtn label="Submit" />
        </form>
    }
}
