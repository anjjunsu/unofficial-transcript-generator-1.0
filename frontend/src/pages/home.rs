use stylist::style;
use yew::prelude::*;

#[function_component(Home)]
pub fn home() -> Html {
    let ss = style!(
        r#"
            h1 {
                font-size: 35px;
                padding: 10px;
            }
            .m1 {
                margin: 10px;
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-content: center;
                justify-content: center;
                text-align: center;
                align-items: center;
            }

            .guide h1 {
                font-size: 30px;
            }
            
            .guide h2 {
                font-size: 25px;
            }

       "#
    )
    .expect("Failed to mount style sheet for Main page");

    html! {
        <>
        <div class={ss}>
            <div class={"m1"}>
                <h1>{ "Unofficial Transcript Generator" }</h1>
                <div class={"guide"}>
                    <h1>{"Upload your undescriptive \"UBC SSC Grade Summary\" PDF file here"}</h1>
                    <h2>{"This generator will add full course name to your transcript"}</h2>
                    <h2>{"And also make it look nice"}</h2>
                    <h2>{"So that reader can understand what you actually studied instead of some random abbreviation🫡"}</h2>
                </div>
            </div>
        </div>
        </>
    }
}
