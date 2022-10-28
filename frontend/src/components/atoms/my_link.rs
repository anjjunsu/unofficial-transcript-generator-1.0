use crate::router::Route;
use stylist::{style, yew::styled_component};
use yew::prelude::*;
use yew_router::prelude::*;

#[derive(Properties, Clone, PartialEq)]
pub struct Props {
    pub text: String,
    pub data_test: String,
    pub route: Route,
}

#[styled_component(MyLink)]
pub fn my_link(props: &Props) -> Html {
    let ss = style!(
        r#"
            font-size: 22px;
            text-decoration: none;
            color: #FFFFFF;    
        "#
    )
    .expect("Failed to mount style sheet for my link");

    html! {
        <span data-test={props.data_test.clone()}>
        <Link<Route>to={props.route.clone()} classes={classes!(ss)}>{props.text.clone()}</Link<Route>>
        </span>
    }
}
