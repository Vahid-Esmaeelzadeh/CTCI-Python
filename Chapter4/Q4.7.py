import copy
# region Solution 1
def buildOrder(projects, dep) -> list:
    prjDict = convertToDict(projects, dep)
    result = []

    while len(prjDict) > 0:
        rootProjects = extractRootProjects(prjDict)

        if len(rootProjects) == 0:
            return []

        for x in rootProjects:
            result.append(x)
            del prjDict[x]

    return result


def convertToDict(projects, dep):
    result = dict()
    for x in projects:
        result[x] = []

    for d in dep:
        result[d[0]].append(d[1])

    return result

def extractRootProjects(prjDict: dict):
    projects = set(prjDict.keys())
    dependent_projects = set()

    for x in prjDict:
        for i in prjDict[x]:
            dependent_projects.add(i)

    return projects - dependent_projects

# endregion
# region DFS-based solution
# will be completed
# endregion

dep = [('a', 'd'), ('f', 'c'), ('d', 'c'), ('f', 'a'), ('f', 'b')]
projects = ['a', 'b', 'c', 'd', 'e', 'f']

print(buildOrder(copy.deepcopy(projects), dep))

