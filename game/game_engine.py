import random
import pygame
from game.button import ChoiceButton

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.choices = ["ROCK", "PAPER", "SCISSORS"]
        btn_w, btn_h = 130, 50
        gap = 20
        total_w = 3 * btn_w + 2 * gap
        start_x = (width - total_w) // 2
        btn_y = height - 85

        self.buttons = [
            ChoiceButton("ROCK", pygame.Rect(start_x, btn_y, btn_w, btn_h), (160, 50, 50), (200, 70, 70)),
            ChoiceButton("PAPER", pygame.Rect(start_x + btn_w + gap, btn_y, btn_w, btn_h), (40, 100, 170), (60, 130, 210)),
            ChoiceButton("SCISSORS", pygame.Rect(start_x + 2 * (btn_w + gap), btn_y, btn_w, btn_h), (180, 140, 30), (220, 180, 50)),
        ]

        self.player_choice = None
        self.cpu_choice = None
        self.result_text = "Make your move!"
        self.result_color = (220, 225, 235)

        self.player_score = 0
        self.cpu_score = 0

        self.round_resolved_time = 0
        self.display_duration = 1800
        self.showing_result = False

        self.font_title = pygame.font.SysFont(None, 36)
        self.font_hud = pygame.font.SysFont(None, 26)
        self.font_arena = pygame.font.SysFont(None, 32)

    def determine_winner(self, player, cpu):
        if player == cpu:
            return "TIE"
        
        # BUG SYMPTOM: 
        # All winning matchups are inverted, causing player choices to lose against what they normally beat.
        rules = {
            ("ROCK", "SCISSORS"): "PLAYER",
            ("SCISSORS", "PAPER"): "PLAYER",
            ("PAPER", "ROCK"): "PLAYER",
            ("SCISSORS", "ROCK"): "CPU",
            ("PAPER", "SCISSORS"): "CPU",
            ("ROCK", "PAPER"): "CPU",
        }
        return rules.get((player, cpu), "TIE")

    def play_round(self, choice):
        self.player_choice = choice
        self.cpu_choice = random.choice(self.choices)

        outcome = self.determine_winner(self.player_choice, self.cpu_choice)
        if outcome == "PLAYER":
            self.player_score += 1
            self.result_text = f"You Win! {self.player_choice} beats {self.cpu_choice}."
            self.result_color = (80, 230, 120)
        elif outcome == "CPU":
            self.cpu_score += 1
            self.result_text = f"You Lose! {self.cpu_choice} beats {self.player_choice}."
            self.result_color = (240, 80, 80)
        else:
            self.result_text = f"It's a Draw! Both picked {self.player_choice}."
            self.result_color = (240, 210, 80)

        self.showing_result = True
        self.round_resolved_time = pygame.time.get_ticks()

    self.showing_result = True
self.round_resolved_time = pygame.time.get_ticks()

if self.player_score >= self.target_score:
    self.game_over = True
    self.winner = "PLAYER"
elif self.cpu_score >= self.target_score:
    self.game_over = True
    self.winner = "CPU"

    def handle_event(self, event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        if self.game_over:
            self.player_score = 0
            self.cpu_score = 0
            self.game_over = False
            self.winner = None
            self.player_choice = 0
            self.cpu_choice = 0
            self.result_text = "Make your move!"
            self.result_color = (220, 225, 235)
            self.showing_result = False
        return

    if self.game_over:
        return

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for btn in self.buttons:
            if btn.contains(event.pos):
                self.play_round(btn.choice_name)
                break

    def update(self):
        now = pygame.time.get_ticks()
        if self.showing_result and (now - self.round_resolved_time >= self.display_duration):
            self.player_choice = None
            self.cpu_choice = None
            self.result_text = "Make your move!"
            self.result_color = (190, 195, 205)
            self.showing_result = False

    def render(self, screen):
        screen.fill((24, 28, 36))

    if self.game_over:
        title = self.font_title.render(
            "GAME OVER",
            True,
            (245, 245, 245)
        )
        screen.blit(
            title,
            (self.width // 2 - title.get_width() // 2, 70)
        )

        if self.winner == "PLAYER":
            winner_text = "PLAYER WINS!"
            winner_color = (80, 230, 120)
        else:
            winner_text = "CPU WINS!"
            winner_color = (240, 80, 80)

        winner_surf = self.font_arena.render(
            winner_text,
            True,
            winner_color
        )
        screen.blit(
            winner_surf,
            (self.width // 2 - winner_surf.get_width() // 2, 130)
        )

        score_text = self.font_hud.render(
            f"Final Score: {self.player_score} - {self.cpu_score}",
            True,
            (225, 225, 230)
        )
        screen.blit(
            score_text,
            (self.width // 2 - score_text.get_width() // 2, 180)
        )

        restart_text = self.font_hud.render(
            "Press R to play again",
            True,
            (190, 195, 205)
        )
        screen.blit(
            restart_text,
            (self.width // 2 - restart_text.get_width() // 2, 230)
        )

        return

    title_surf = self.font_title.render("Rock Paper Scissors", True, (245, 245, 245))

        title_surf = self.font_title.render("Rock Paper Scissors", True, (245, 245, 245))
        screen.blit(title_surf, (self.width // 2 - title_surf.get_width() // 2, 14))

        p_surf = self.font_hud.render(f"Player Score: {self.player_score}", True, (100, 180, 255))
        c_surf = self.font_hud.render(f"CPU Score: {self.cpu_score}", True, (255, 120, 120))
        screen.blit(p_surf, (35, 52))
        screen.blit(c_surf, (self.width - c_surf.get_width() - 35, 52))

        pygame.draw.line(screen, (45, 52, 66), (25, 82), (self.width - 25, 82), 2)

        p_str = self.player_choice if self.player_choice else "--"
        c_str = self.cpu_choice if self.cpu_choice else "--"

        arena_p = self.font_arena.render(f"Your Pick:  {p_str}", True, (225, 225, 230))
        arena_c = self.font_arena.render(f"CPU Pick:  {c_str}", True, (225, 225, 230))
        screen.blit(arena_p, (self.width // 2 - arena_p.get_width() // 2, 115))
        screen.blit(arena_c, (self.width // 2 - arena_c.get_width() // 2, 155))

        res_surf = self.font_arena.render(self.result_text, True, self.result_color)
        screen.blit(res_surf, (self.width // 2 - res_surf.get_width() // 2, 205))

        for btn in self.buttons:
            btn.render(screen)
