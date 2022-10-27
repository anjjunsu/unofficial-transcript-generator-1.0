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
                padding: 10px;
                font-size: 40px;
                font-weight: 600;
                color: #337EA9;  
            }

            .social_card h2 {
                font-size: 30px;
                color: black;
                padding: 5px;
            }

            .r1 {
                display: flex;
                flex-direction: row;
                align-items: center;
                align-contents: center;
                justify-content: center;
            }

            h1 {
                padding: 20px;
                font-size: 50px;
                font-weight: 700;
                display: flex;
                align-items: center;
            }
            
            h2 {
                padding: 10px;
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
                    <div class={"r1"}>
                        <a href={"https://www.instagram.com/anjjunsu/"}>
                        <img alt={"Link to GitHub"}
                            src={"https://github.com/anjjunsu/unofficial-transcript-generator/blob/main/frontend/src/assets/images/logo-ig-png-32456.png?raw=true"}
                            width={"32"}
                            height={"32"} />
                        <h2>{"@anjjunsu"}</h2>
                        </a>
                    </div>
                </div>
                <div class={"social_card"}>
                    <h1>{"GitHub"}</h1>
                    <a href={"https://github.com/anjjunsu"}>
                        <img alt={"Link to Instagram"}
                            src={"https://github.com/anjjunsu/unofficial-transcript-generator/blob/main/frontend/src/assets/images/GitHub-Mark-32px.png?raw=true"}
                            width={"32"}
                            height={"32"} />
                    </a>
                </div>
                <div class={"social_card"}>
                    <h1>{"LinkedIn"}</h1>
                    <a href={"https://www.linkedin.com/in/junsu-an"}>
                        <img alt={"Link to LinkedIn"}
                            src={"https://github.com/anjjunsu/unofficial-transcript-generator/blob/main/frontend/src/assets/images/LI-In-Bug.png?raw=true"}
                            width={"32"}
                            height={"32"} />
                    </a>
                </div>
                </div>
            </div>
        </div>
        </>
    }
}
