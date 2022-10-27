use crate::components::atoms::my_link::MyLink;
use crate::router::Route;
use stylist::{style, yew::styled_component};
use yew::prelude::*;

#[styled_component(Navbar)]
pub fn navbar() -> Html {
    let ss = style!(
        r#"
            section {
                padding: 10px 15px;
                background-color: rgba(51, 126, 169, 1);
                display: flex;
                justify-content: space-between;
            }
        "#
    )
    .expect("Failed to mount css for Navbar");

    html! {
        <div class={ss}>
          <section>
            <MyLink text="Unofficial Transcript Generator" data_test="logo" route={Route::Home} />
          </section>
        </div>
    }
}
