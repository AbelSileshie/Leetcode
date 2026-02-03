SELECT name AS Employee
FROM Employee e
WHERE managerID IS NOT NULL
  AND salary > (SELECT salary FROM Employee WHERE id = e.managerID)
ORDER BY name;
