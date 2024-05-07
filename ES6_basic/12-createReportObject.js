export default function createReportObject(employeesList) {
  return {
    allEmployees: {...employeesList},
    getNumberOfDepartments(employeesList = this.allEmployees) {
        return Object.keys(employeesList).length;
    }
  };
}
