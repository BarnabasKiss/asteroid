import pygame
from constants import *
from circleshape import CircleShape
from shots import Shot


class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shot_timer = 0

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]


	def update(self, dt):
		keys = pygame.key.get_pressed()

		if self.shot_timer > 0:
			self.shot_timer -= dt

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
			self.move(dt * 2)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()
		

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
		
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt


	def shoot(self):
		if self.shot_timer <= 0:
			shot = Shot(self.position.x, self.position.y)
			shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
			self.shot_timer += PLAYER_SHOOT_COOLDOWN