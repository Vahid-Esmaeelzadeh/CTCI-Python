import math
def buildOrder(projects: list, dependencies: list) -> list:
    result = []
    adjDict = convertToDict(dependencies, projects)

    while len(adjDict) > 0:
        rootProjects = extractRootProjects(adjDict, projects)

        if len(rootProjects) == 0:
            return "Error"

        for x in rootProjects:
            result.append(x)

        removeProjects(adjDict, projects, rootProjects)

    return result


def convertToDict(d, projects):
    result = dict()
    for x in projects:
        result[x] = []

    val = []

    for x in d:
        result[x[0]].append(x[1])

    return result

def extractRootProjects(adjDict, projects):
    dependent_projects = set()
    for x in adjDict:
        for i in adjDict[x]:
            dependent_projects.add(i)

    return list(set(projects) - dependent_projects)


def removeProjects(adjDict, projects, rootProjects):
    for x in rootProjects:
        del adjDict[x]
        projects.remove(x)


dep = [('a', 'd'), ('f', 'c'), ('d', 'c'), ('f', 'a'), ('f', 'b')]
projects = ['a', 'b', 'c', 'd', 'e', 'f']

print(buildOrder(projects, dep))


