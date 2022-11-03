# DAO (Data Access Object)#
DAO o "Objeto de Acceso a Datos" en español, es la relacion que tiene 
una aplicacion hacia uno mucho dispositivos tecnologicos que lleven
a cabo el almacenamiento de datos, esto se puede describir como 
una base de datos o simplemente como un archivo. 
Esto tiene una gran ventaja al utilizar DAO y es que la aplicacion 
donde se este trabajando puede ser modificada o actualizada sin cambiar
partes de la aplicacion.


public void createUser(NewUserRequestDTO dto) {  

    UserDAO userDAO = new UserDAOImpl();  
        
    if(userDAO.findByUsername(dto.getUsername()) != null) {  
        throw new RuntimeException("Username already exists");  
    }  
        
    UserConverter usrConverter = new UserConverter();  
    User user = surConverter.fromDto(dto);  
    
    usrDAO.save(user);  
}
