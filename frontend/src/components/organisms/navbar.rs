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
                justify-content: space-around;
            }

            a {
                text-decoration: none;
                color: #FFFFFF;
            }
        "#
    )
    .expect("Failed to mount css for Navbar");

    html! {
        <div class={ss}>
          <section>
            <MyLink text="Unofficial Transcript Generator" data_test="logo" route={Route::Home} />
            <MyLink text="Guide" data_test="logo" route={Route::Guide} />
            <a class={"github-button"}
                href={"https://github.com/anjjunsu/unofficial-transcript-generator"}
                data-icon={"octicon-star"}
                data-size={"large"}
                data-show-count={"true"}
                aria-label={"Star anjjunsu/unofficial-transcript-generator on GitHub"}>
                {"Star"}
            </a>
          </section>
        </div>
    }
}
