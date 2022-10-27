mod components;
mod pages;
mod router;

use components::organisms::{footer::Footer, navbar::Navbar};
use router::{switch, Route};
use yew::prelude::*;
use yew_router::prelude::*;

#[function_component(App)]
pub fn app() -> Html {
    html! {
        <>
            <BrowserRouter>
                <Navbar />
                <Switch<Route> render={Switch::render(switch)} />
                <Footer />
            </BrowserRouter>
        </>
    }
}
