import litellm
litellm.drop_params = True
litellm.modify_params = True

from .agent import root_agent
