policy_factory = dict()


def none_policy():
    return None


from crowd_nav.policy.orca import ORCA
from crowd_nav.policy.social_force import SOCIAL_FORCE
from crowd_nav.policy.srnn import SRNN

policy_factory["orca"] = ORCA
policy_factory["none"] = none_policy
policy_factory["social_force"] = SOCIAL_FORCE
policy_factory["srnn"] = SRNN
# TODO: specify ConvGRU policy
policy_factory['convgru'] = SRNN
