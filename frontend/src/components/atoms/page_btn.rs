use crate::components::atoms::my_link::MyLink;
use crate::router::Route;
use stylist::style;
use yew::prelude::*;

#[derive(Properties, PartialEq)]
pub struct Props {
    pub label: String,
    pub route: Route,
}

#[function_component(PageBtn)]
pub fn page_btn(props: &Props) -> Html {
    let ss = style! {
        r#"
            color: white; 
            background-color: rgba(51, 126, 169, 1);
            font-family: iawriter-mono, Nitti, Menlo, Courier, monospace;
            font-weight: bold;
            padding: 15px;
            margin: 10px;
            border-color: white;
        "#
    }
    .expect("Failed to mount style sheet for page button");

    html! {
        <button class={ss}>
            <MyLink text={props.label.clone()}
                    data_test=""
                    route={props.route.clone()}/>
        </button>
    }
}
