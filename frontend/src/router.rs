use crate::pages::{contact::Contact, guide::Guide, home::Home};
use yew::prelude::*;
use yew_router::prelude::*;

#[derive(Clone, Routable, PartialEq)]
pub enum Route {
    #[at("/")]
    Home,
    #[at("/contact")]
    Contact,
    #[at("/guide")]
    Guide,
    #[not_found]
    #[at("/404")]
    NotFound,
}

pub fn switch(routes: &Route) -> Html {
    match routes {
        Route::Home => html! { <Home /> },
        Route::Contact => html! { <Contact /> },
        Route::Guide => html! { <Guide /> },
        Route::NotFound => html! { "Not Found" },
    }
}
