from papermerge-restapi-client.paths.api_nodes_id_tags_.post import ApiForpost
from papermerge-restapi-client.paths.api_nodes_id_tags_.delete import ApiFordelete
from papermerge-restapi-client.paths.api_nodes_id_tags_.patch import ApiForpatch


class ApiNodesIdTags(
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
