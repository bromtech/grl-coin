import asyncio
import flet as ft
from db import Database
from flet import Page, Row, MainAxisAlignment, TextField, TextAlign, Column, ElevatedButton



async def main(page: Page) -> None:
	db = Database('database.db')
	page.vertical_alignment = MainAxisAlignment.CENTER
	#page.window_width = 500
	#page.window_height = 700
	#page.window_resizable = False
	page.title = "Banana Clicker"
	page.theme_mode = ft.ThemeMode.DARK
	page.bgcolor = "#141221"
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.fonts = {"ofont.ru_Fulbo Argenta": "fonts/ofont.ru_Fulbo Argenta.ttf"}
	page.theme =  ft.Theme(font_family="ofont.ru_Fulbo Argenta")

	
	async def auth(event: ft.ContainerTapEvent) -> None:
		_login = login_input.value

		if db.user_exists(_login):
			page.remove(login_input)
			authorize_button.visible = False
			async def score_up(event: ft.ContainerTapEvent) -> None:
				score.data += 1
				score.value = str(score.data)

				image.scale = 0.95

				score_counter.opacity = 50
				score_counter.value = ""
				score_counter.right = 0
				score_counter.left = event.local_x
				score_counter.top = event.local_y
				score_counter.bottom = 0

				progress_bar.value += (1 / 100)

				if score.data % 100 == 0:
					page.snack_bar = ft.SnackBar(
						content=ft.Text(
							value="🍌 +1",
							size=20,
							color="#ffec1f",
							text_align=ft.TextAlign.CENTER
						),
						bgcolor="#25223a"
					)
					db.add_click(_login)
					page.snack_bar.open = True
					progress_bar.value = 0

				await page.update_async()

				await asyncio.sleep(0.1)
				image.scale = 1
				score_counter.opacity = 0

				await page.update_async()

			score = ft.Text(value="0", size=100, data=0)
			score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
			image = ft.Image(src="banana.png", fit=ft.ImageFit.CONTAIN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))

			progress_bar = ft.ProgressBar(
				value=0, #0-1
				width=page.width - 100, 
				bar_height=20,
				color="#ffec1f",
				bgcolor="#bfa524"
			)

			await page.add_async(
				score,
				ft.Container(
					content=ft.Stack(controls=[image, score_counter]),
					on_click=score_up,
					margin=ft.Margin(0, 0, 0, 30)
				),
				ft.Container(
					content=progress_bar,
					border_radius=ft.BorderRadius(10, 10, 10, 10)
				)
			)


	login_input = TextField(text_align=TextAlign.CENTER, label="ID")
	authorize_button = ElevatedButton("Authorize", on_click=auth)

	page.add(
		login_input,
		authorize_button
	)

if __name__ == "__main__":
	ft.app(target=main, view=ft.WEB_BROWSER)