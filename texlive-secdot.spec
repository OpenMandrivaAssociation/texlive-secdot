%global tl_name secdot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Section numbers with trailing dots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/secdot
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Makes the numbers of \section commands come out with a trailing dot.
Includes a command whereby the same can be made to happen with other
sectioning commands.

