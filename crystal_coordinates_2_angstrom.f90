program crystal_angstrom
implicit none
real:: a,b,c
integer::i,j
Integer,parameter::natm=8
real,allocatable :: posxyz(:,:) , posxyz_angs(:,:)
character (len = 8), dimension (natm) :: atms
print*,"give a,b,c in angstrom"
!read*,a
!read*,b
!read*,c
a=7.830791978 ! Give for your hexagonal system
b=7.830791978
c=22.208050878
!a=14.798051111833407
!b=14.798051111833407
!c=41.967130899574556
allocate (posxyz(natm,3))
allocate (posxyz_angs(natm,3))

open (unit=100, file='coordinate_x.dat') ! Create x-coordinates to read as input
open (unit=200, file='coordinate_y.dat') ! same for y
open (unit=300, file='coordinate_z.dat') ! same for z
open (unit=400, file='atom_name.dat')    ! Give list of elements' name.
do j=1,natm
 read(100,*) posxyz(j,1) 
 read(200,*) posxyz(j,2)
 read(300,*) posxyz(j,3)
 read(400,*) atms(j)
end do

do i=1,natm
! print*, "crys_coord",posxyz(i,1),posxyz(i,2), posxyz(i,3)
 posxyz_angs(i,1)= a*posxyz(i,1)                        
 posxyz_angs(i,2)= a*(posxyz(i,1)*0.500000 - posxyz(i,2)*.86602540378443864676)
 posxyz_angs(i,3)=posxyz(i,3)*c
 print*,atms(i), posxyz_angs(i,1),posxyz_angs(i,2), posxyz_angs(i,3)
enddo

deallocate (posxyz_angs)
deallocate (posxyz)
end program
