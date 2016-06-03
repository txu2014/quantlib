
"""
 Copyright (C) 2005, 2006, 2007 Eric Ehlers
 Copyright (C) 2005 Plamen Neykov
 Copyright (C) 2005 Aurelien Chanudet

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it
 under the terms of the QuantLib license.  You should have received a
 copy of the license along with this program; if not, please email
 <quantlib-dev@lists.sf.net>. The license is also available online at
 <http://quantlib.org/license.shtml>.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

"""Encapsulate enumerations for a library datatype."""

from gensrc.serialization import serializable
from gensrc.utilities import common

class EnumeratedClass(serializable.Serializable):
    """Encapsulate a string->value mapping for a library enumerated class."""

    #############################################
    # class variables
    #############################################

    groupName_ = 'EnumeratedClasses'

    #############################################
    # public interface
    #############################################

    def string(self):
        """Return the string identifying this enumeration."""
        return self.string_

    def value(self):
        """Return the value of this enumeration."""
        return self.value_

    def libraryClass(self):
        """Return the type of this enumeration."""
        return self.libraryClass_

    #############################################
    # serializer interface
    #############################################

    def name(self):
        """Return unique identifier for this object."""
        return self.string_

    def serialize(self, serializer):
        """Load/unload class state to/from serializer object."""
        serializer.serializeProperty(self, common.STRING)
        serializer.serializeProperty(self, common.VALUE)
        serializer.serializeProperty(self, common.LIBRARY_CLASS)

class EnumeratedClassGroup(serializable.Serializable):
    """Encapsulate a group of EnumeratedClass objects."""

    #############################################
    # class variables
    #############################################

    groupName_ = 'EnumeratedClassGroups'

    #############################################
    # public interface
    #############################################

    def className(self):
        """Return the class relating to this EnumeratedClassGroup object."""
        return self.class_

    def enumeratedClasses(self):
        """Serve up enumerated classes alphabetically by name."""
        for key in self.enumeratedClassKeys_:
            yield self.enumeratedClasses_[key]

    def includeFile(self):
        """Return #include directive necessary to compile the source
        code autogenerated in relation to this class."""
        return self.includeFile_

    #############################################
    # serializer interface
    #############################################

    def name(self):
        """Return unique identifier for this object."""
        return self.class_

    def serialize(self, serializer):
        """Load/unload class state to/from serializer object."""
        serializer.serializeAttribute(self, 'class')
        serializer.serializeObjectDict(self, EnumeratedClass)
        serializer.serializeProperty(self, 'includeFile')
        serializer.serializeAttributeBoolean(self, 'need_ptr', True)
