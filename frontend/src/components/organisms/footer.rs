use crate::components::atoms::my_link::MyLink;
use crate::router::Route;
use stylist::{style, yew::styled_component};
use yew::prelude::*;

#[styled_component(Footer)]
pub fn footer() -> Html {
    let ss = style!(
        r#"
            * {
                display: flex;
                justify-content: space-between;
                font-size: 20px;
                color: #FFFFFF;
                box-sizing: border-box;
            }
            section {
                padding: 10px 15px;
                background-color: rgba(51, 126, 169, 1);
                display: flex;
                justify-content: space-between;
            }

            a {
                text-decoration: none;
            }
        "#
    )
    .expect("Failed to mount css for Footer");

    html! {
        <div class={ss}>
          <section>
            <a href="https://github.com/anjjunsu/unofficial-transcript-generator/issues">{ "Report a bug" }</a>
            <MyLink text="Contact" data_test="" route={Route::Contact} />
          </section>
        </div>
    }
}
