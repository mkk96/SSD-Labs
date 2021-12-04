use company;

-- Question 1 --

select concat(Fname, ' ', Lname) as "Full Name", Ssn 
from employee e 
where Ssn in 
	(select mgr_ssn  
	from department d
	where Dnumber in 
		(select distinct Dno 
		from employee e 
		where Ssn in 
			(select Essn 
			from works_on wo 
			group by Essn 
			having sum(Hours) < 40)
		)
	);


-- Question 2 --

(select concat(Fname," ", Lname) as "Full Name", Ssn, cnt, Dname from 
(select e.*, Dname from department d join employee e on e.Dno = d.Dnumber ) e2 join
(select  distinct Super_ssn, count(*) as cnt from employee e 
where Super_ssn is not null 
group by Super_ssn) as temp
on temp.Super_ssn = e2.ssn
order by cnt);


-- Question 3 --

select Essn, count(*) from works_on wo
where Essn in  (select Mgr_ssn from department d where Dnumber in 
(select Dnum from project p where Pname = "ProductY"));

-- Question 4 --


SELECT d.dnumber, d.dname, count(dl.dlocation) as "Number of locations" from department d INNER JOIN (
SELECT essn from dependent where sex = 'F' group by essn having count(Dependent_name) > 1
) de on d.Mgr_ssn = de.essn
INNER JOIN dept_locations dl on dl.dnumber = d.dnumber
GROUP BY d.dnumber, d.dname;


-- Question 5 --

select Essn, count(*) from dependent d
where Essn in (select Mgr_ssn from department d  where Dnumber in (select Dnumber from dept_locations as dl
group by Dnumber 
having count(*) >= 2));