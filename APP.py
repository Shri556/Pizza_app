import flet as ft

def main(page:ft.Page):
    page.title = "FINAL APP"
    #page.theme_mode = "light"
    page.bgcolor = ft.colors.BLACK87
    
    page.fonts = {
        "Tw":"./fonts/TravelingTypewriter.ttf"
    }
    email = ft.TextField(hint_text="email id...",width=300,border_radius=20,border_color=ft.colors.YELLOW_ACCENT)
    password = ft.TextField(hint_text="password...",width=300,border_radius=20,border_color=ft.colors.YELLOW_ACCENT,password=True,can_reveal_password=True)
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Pizza Store",size=40,font_family="Tw"), bgcolor=ft.colors.BACKGROUND,color=ft.colors.YELLOW_ACCENT,center_title=True,),
                    email,
                    password,
                    ft.Container(height=10),
                    ft.ElevatedButton("Go to Store",on_click=go_to_welcome,height=40,color=ft.colors.AMBER),
                ],
                vertical_alignment="center",
                horizontal_alignment="center",
                padding=100,
                scroll="always"
            )
        )
        
        if page.route == "/welcome" or page.route == "/welcome/oreder-summary":
            page.views.append(
                ft.View(
                    "/welcome",
                    [
                        ft.AppBar(title=ft.Text("WELCOME!"),center_title=True,color=ft.colors.YELLOW_ACCENT),
                        ft.Row([ft.Image(src="images/capsicum.png",width=400),ft.Image(src="images/onion.png",width=400,)],alignment="center"),
                        ft.Row([ft.Image(src="images/onion.png",width=400),ft.Image(src="images/watermelon.png",width=400)],alignment="center"),
                        ft.Row([ft.ElevatedButton("Add all items to the cart",on_click=lambda _: page.go("/welcome/a")),ft.ElevatedButton("Logout",on_click=lambda _: page.go("/"))],alignment="center"),
                    ],
                    scroll="always",
                    vertical_alignment= "center",
                    horizontal_alignment="center"
                )
            )
            
        if page.route == "/welcome/a":
            page.views.append(
                ft.View(
                    "/welcome/order_summary",
                    [
                        ft.AppBar(title=ft.Text("Summary",color=ft.colors.YELLOW_ACCENT),bgcolor=ft.colors.BACKGROUND),
                        ft.Text("="*138),
                        ft.Row([ft.Text("ORDER DETAILS",weight="bold",font_family="Tw",style="titleLarge")],alignment="center"),
                        ft.Text("="*138),
                        ft.Text("1. Tomato Pizza [1 Qty] = ₹ 200/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("2. Onion Pizza [1 Qty] = ₹ 250/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("3. Capsicum Pizza [1 Qty] = ₹ 250/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("4. Watermelon Pizza [1 Qty] = ₹ 200/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("First order free delivery = ₹ 0/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("="*138),
                        ft.Text("Total Payable Amount = ₹ 900/-",weight="bold",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("="*138),
                        ft.Container(height=50),
                        ft.ElevatedButton("Back to Homepage",on_click=lambda _: page.go("/welcome"))
                    ],
                    horizontal_alignment="center",
                    vertical_alignment="center",
                    scroll="always",
                    padding=60
                )
            )
        page.update()
        
    def view_top(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    def go_to_welcome(e):
        if not email.value:
            email.error_text = "Enter a Email"
            password.error_text = ""
        elif not password.value:
            email.error_text = ""
            password.error_text = "Enter a Password"
        else:
            email.error_text = ""
            password.error_text = ""
            email.value = ""
            password.value = ""
            page.go("/welcome")
        page.update()
        
    page.on_route_change = route_change
    page.on_view_pop = view_top
    page.go(page.route)

ft.app(target=main,assets_dir="assets")