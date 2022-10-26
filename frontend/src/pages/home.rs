use yew::prelude::*;

#[function_component(Home)]
pub fn home() -> Html {
    html! {
        <>
            <h1>{ "Home page title" }</h1>
            <div>{ "Home page body" }</div>
        </>
    }
}
