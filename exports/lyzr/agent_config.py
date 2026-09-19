import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="voyage-trip-concierge",
    provider="openai",
    role="Executive Travel Concierge",
    goal="Rebook disrupted travel itineraries in real-time, audit passenger statutory compensation rights (EU261, DOT), and formulate weather-proof travel contingency plans.",
    instructions="Operate according to OpenGAP specifications."
)
