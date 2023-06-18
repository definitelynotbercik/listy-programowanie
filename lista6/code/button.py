import pygame

class Button():
	def __init__(self, position, image, scale, text):
		"""
		Initialize a Button object.

        Args:
            position (tuple): The position of the button's center point (x, y).
            image (Surface): The button's image.
            scale (float): The scaling factor for the button's image.
            text (str): The text to display on the button.
        """

		width = image.get_width()
		height = image.get_height()
		self.font = pygame.font.Font("semestr2\\lista6\\font\\Pixeltype.ttf", 50)
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.text = self.font.render(text, False, (255,255,255))
		self.text_rect = self.text.get_rect(center = position)
		self.rect = self.image.get_rect(center = position)
		self.clicked = False

	def draw(self, surface):
		"""
		Draw the button on the screen and check for user interaction.

        Args:
            surface (Surface): The surface to draw the button on.

        Returns:
            bool: True if the button is clicked, False otherwise.
        """

		action = False

		# Mouse position
		pos = pygame.mouse.get_pos()

		# Check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# Draw button on screen
		surface.blit(self.image, self.rect)
		surface.blit(self.text, self.text_rect)

		return action
	