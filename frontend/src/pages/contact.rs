use stylist::style;
use yew::prelude::*;

#[function_component(Contact)]
pub fn contact() -> Html {
    let ss = style!(
        r#"
            .m1 {
                text-align: center;
                display: flex;
                flex-direction: column;
                align-items: center;
                align-contents: center;
                justify-content: center;
                width: 100%;
                max-width: 100%;
            }

            .social_media {
                display: flex;
                flex-direction: row;
            }

            .social_card {
                padding: 20px;
                align-items: center;
                align-contents: center;
                justify-content: center;
            }

            .social_card h1 {
                padding: 5px;
                font-size: 40px;
                font-weight: 600;
                color: #337EA9;  
            }

            .social_card h2 {
                font-size: 30px;
                color: black;
                padding: 5px;
            }

            h1 {
                padding: 20px;
                font-size: 50px;
                font-weight: 700;
                display: flex;
                align-items: center;
            }
            
            h2 {
                padding: 15px;
                font-size: 40px;
                font-weight: 600;
                color: #337EA9;  
            }

            a {
                font-size: 30px;
                text-decoration: none;
                color: black;
            }
        "#
    )
    .expect("Failed to mount css for Contact page");

    html! {
        <>
        <div class={ss}>
            <div class={"m1"}>
                <br />
                <h1>{"Junsu An"}</h1>
                <h2>{"Email"}</h2>
                <a href={"mailto:anjjunsu@gmail.com"}>{"anjjunsu@gmail.com"}</a>
                <br />
                <div class={"social_media"}>
                <div class={"social_card"}>
                    <h1>{"Instagram"}</h1>
                    <h2>{"@anjjunsu"}</h2>
                </div>
                <div class={"social_card"}>
                    <h1>{"GitHub"}</h1>
                    <svg xmlns={"http://www.w3.org/2000/svg"}
                        width={ "35" }
                        height={ "35" }
                        viewBox={ "0 0 24 24" }>
                        <a xlink:href={"https://github.com/anjjunsu"} target="_top">
                            <path d={"M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"}/>
                        </a>
                    </svg>
                </div>
                <div class={"social_card"}>
                    <h1>{"LinkedIn"}</h1>
                </div>
                </div>
            </div>
        </div>
        </>
    }
}
